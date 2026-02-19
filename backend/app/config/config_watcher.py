from app.config_reader import reload_readers_with_namespace
from app.utils.list_helpers import map_as_list, filter_as_list
from app.utils.singleton_meta import SingletonMeta
from watchdog.observers.api import BaseObserver
from app.utils.logger import logger
import atexit
import time
from typing import Callable
from ntpath import join
from genericpath import isfile
from os import listdir
from watchdog.events import FileSystemEventHandler, FileModifiedEvent, DirModifiedEvent
from watchdog.observers import Observer

class ConfigWatcher(metaclass=SingletonMeta):
    allow_reporting = True

    def __init__(self):
        conf_dir = "config/"
        self.configs = [(f.split('.')[0], join(conf_dir, f)) for f in listdir(conf_dir) if isfile(join(conf_dir, f))]
        self.configs = filter_as_list(lambda c: c[0] != '', self.configs) # filter out some swap files

        self.observers: list[BaseObserver] = []
        for (namespace, conf_file) in self.configs:
            self.observers.append(self._init_watcher(conf_file, namespace))
        logger.info(f"started watching config files for changes: {str(map_as_list(lambda c: c[1], self.configs))}")

        atexit.register(self._stop_all_observers)

    def _init_watcher(self, path: str, namespace: str):
        observer = Observer()
        self.handler = FileModifiedHandler(path, lambda: self._handle_config_update(namespace))
        observer.schedule(self.handler, path)
        observer.start()
        return observer

    def _stop_all_observers(self):
        for observer in self.observers:
            observer.stop()

    def _handle_config_update(self, namespace: str):
        if namespace == "":
            return
        if not self.allow_reporting:
            return
        logger.info(f"Detected config file update. Reloading config readers in namespace: {namespace}")
        reload_readers_with_namespace(namespace)

    # used to prevent redundant configReader reloads when updating config via api
    def prevent_update_reporting(self):
        self.allow_reporting = False

    def allow_update_reporting(self):
        self.allow_reporting = True

class FileModifiedHandler(FileSystemEventHandler):
    def __init__(self, path: str, callback: Callable):
        self.path = path
        self.callback = callback
        self.last_trigger = time.time()

    def on_modified(self, event: DirModifiedEvent | FileModifiedEvent):
        # necessary for deduping modified events when python edits config
        if (time.time() - self.last_trigger) > 1:
            self.callback()
            self.last_trigger = time.time()

