<template>
  <div class="p-4 flex gap-4 flex-col">
    <UAlert v-if="failed" color="error" title="Failed to load configs" />
    <ConfigSkeleton v-if="!loaded" />
    <UTabs v-if="!failed && loaded" :items="items" :unmountOnHide="false">
      <template #mailValidation>
        <ConfigMailValidation :config="(mailValidation as object)" @submit="submitConfig" />
      </template>
      <template #realtimeCheck>
        <ConfigRealtime :config="(contentCheck as object)" @submit="submitConfig" />
      </template>
    </UTabs>
  </div>
</template>

<script lang="ts" setup>
import type { TabsItem } from '@nuxt/ui'
import { TITLE_SUFFIX } from '~/assets/data/appData';
import { CONFIG_PATH } from '~/assets/ts/backendConnector';

const toast = useToast();
useHead({
  title: 'Configure Endpoints' + TITLE_SUFFIX
});

const items: TabsItem[] = [
  {
    label: 'Mail Validation',
    icon: 'lucide-mail',
    slot: 'mailValidation'
  },
  {
    label: 'Realtime Content Check',
    icon: 'lucide-clock',
    slot: 'realtimeCheck'
  }
];

const mailValidation = await getConfig("mail_validation");
const contentCheck = await getConfig("content_check");

const loaded = ref(false);
const failed = ref(false);
onBeforeMount(() => {
  failed.value = mailValidation === undefined || contentCheck === undefined;
  
  if (failed.value) {
    showFail("Failed to load config from backend.");
  }
  loaded.value = true;
});

async function getConfig(namespace: string) {
  try {
    const path = `${CONFIG_PATH}?namespace=${namespace}`;
    return await $fetch<object>(path);
  } catch {  
    return undefined;
  }
}

async function submitConfig(config: object, namespace: string) {
  const body = { 'namespace': namespace, 'content': config };
  try {
    const result = await $fetch<{ code: string }>(CONFIG_PATH, { method: 'POST', body: body });
    if (result.code === "OK") {
      showSuccess();
      return
    }
  } catch { /* empty */ }
  showFail("Failed to update config in the backend.");
}

function showSuccess() {
  toast.add({
    title: 'Success',
    description: 'Updated config in the backend.',
    icon: 'lucide-check',
    color: 'success'
  });
}
function showFail(description: string) {
  toast.add({
    title: 'Failed',
    description: description,
    icon: 'lucide-x',
    color: 'error',
    duration: 5000
  });
}
</script>

<style>

</style>