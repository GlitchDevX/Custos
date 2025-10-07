<template>
    <div id="get-started" class="flex justify-center items-center">
        <div class="w-3xl max-w-full">
            <div class="max-w-xl">
                <h2 class="text-3xl font-bold">
                    Start with Docker Compose
                </h2>
                <p class="muted-text">
                    You can start off by simply creating a new directory with a docker-compose.yaml and this content.
                </p>
            </div>

            <div class="flex flex-row gap-2 mt-4 max-sm:flex-col">
                <UCard class="max-sm:flex max-sm:justify-center">
                    <span class="text-xl font-bold">
                        Configure Compose
                    </span>
                    <USwitch v-model="state.ui" label="User Interface" class="mt-4" />
                    <UFormField label="Backend Port" class="mt-4">
                        <UInputNumber
                        v-model="state.backendPort"
                        orientation="vertical"
                        :formatOptions="{ useGrouping: false, style: 'decimal' }" />
                    </UFormField>
                    <UFormField label="Frontend Port" class="mt-2" :class="{ 'low-opacity': !state.ui }">
                        <UInputNumber
                        v-model="state.frontendPort"
                        orientation="vertical"
                        :formatOptions="{ useGrouping: false, style: 'decimal' }" />
                    </UFormField>
                </UCard>
                <CodeBlock :content="compose" :showCopy="true" language="yaml" class="max-w-[500px] grow" />
           </div>
        </div>
    </div>
</template>

<script lang="ts" setup>
import base from '~/assets/data/compose-pieces/base.yaml?raw';
import uiPart from '~/assets/data/compose-pieces/ui.yaml?raw';

const state = reactive({
    ui: true,
    backendPort: 3060,
    frontendPort: 3070,
});

const compose = computed(() => {
    let str = base;
    const ui = state.ui ? uiPart + "\n" : "";
    str = str.replace("<<UI_PART>>", ui);

    str = str.replace("<<BACKEND_PORT>>", state.backendPort.toString());
    str = str.replace("<<FRONTEND_PORT>>", state.frontendPort.toString());

    return str;
})
</script>

<style>

</style>