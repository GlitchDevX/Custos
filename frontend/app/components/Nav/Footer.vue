<template>
    <div>
        <USeparator class="w-full" />
        <div class="flex justify-center items-center flex-row gap-4 mt-4 mb-4">
            <UButton variant="soft" color="neutral" to="https://github.com/GlitchDevX/custos" target="_blank">
                <UIcon name="lucide:github" />
            </UButton>
            <USeparator orientation="vertical" class="h-4" :decorative="true" />
            <span class="text-dimmed">
                Made with ☕ by
                <ULink to="https://glitchdev.me" target="_blank" >GlitchDev</ULink>
            </span>
        </div>
    </div>
</template>

<script lang="ts" setup>


</script>

<style></style>