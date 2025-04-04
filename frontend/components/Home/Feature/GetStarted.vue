<template>
    <div id="get-started" class="flex justify-center items-center">
        <div class="w-3xl">
            <div class="max-w-xl">
                <h2 class="text-3xl font-bold">
                    Start with Docker Compose
                </h2>
                <p class="muted-text">
                    You can start off by simply creating a new directory with a docker-compose.yaml and this content.
                </p>
            </div>

            <div class="flex flex-row gap-2 mt-4">
                <UCard>
                    <span class="text-xl font-bold">
                        Configure Compose
                    </span>
                    <USwitch v-model="state.ui" label="User Interface" class="mt-4" />
                    <UFormField label="Database Username" class="mt-2">
                        <UInput v-model="state.user" />
                    </UFormField>
                    <UFormField label="Database Password" class="mt-2">
                        <UInput v-model="state.password" />
                    </UFormField>
                </UCard>
                <CodeBlock :content="compose" :showCopy="true" language="yaml" class="max-w-[500px]" />
           </div>
        </div>
    </div>
</template>

<script lang="ts" setup>
import base from '~/assets/data/compose-pieces/base.yaml?raw';
import ui from '~/assets/data/compose-pieces/ui.yaml?raw';
import db from '~/assets/data/compose-pieces/db.yaml?raw';

const state = reactive({
    ui: true,
    user: "custos_user",
    password: ""
});

const compose = computed(() => {
    let str = base;
    if (state.ui) {
        str += "\n" + ui;
    }
    str += "\n" + db;

    str = str.replaceAll('<<user>>', state.user);
    str = str.replaceAll('<<password>>', state.password);

    return str;
})
</script>

<style>

</style>