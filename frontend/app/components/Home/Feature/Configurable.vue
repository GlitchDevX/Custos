<template>
    <div class="flex justify-center items-center">
        <div class="w-3xl relative">
            <div class="max-w-xl">
                <h2 class="text-3xl font-bold flex flex-row gap-2 justify-start items-center">
                    Easily Configurable
                </h2>
                <p class="muted-text">
                    Either configure Custos in the Web-UI or simply edit the json files in the backend.
                </p>
            </div>
            <div class="flex flex-row justify-between items-center mt-2 max-sm:flex-col max-sm:gap-4">
              <NuxtImg src="config_ui.png" class="sm:w-[45%] max-sm:w-[80%] border-2 border-[var(--ui-border)] rounded-xl" />
              <USeparator orientation="vertical" size="xl" class="h-[200px] max-sm:hidden" label="Or" />
              <USeparator orientation="horizontal" size="xl" class="sm:hidden" label="Or" />
              <CodeBlock :content="mailValidation" language="json" textSize="md" />
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>
import mailValidation from '~/assets/data/mail-validation.json?raw';

</script>

<style>

</style>