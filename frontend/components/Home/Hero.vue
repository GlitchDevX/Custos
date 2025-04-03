<template>
<div class="flex flex-col items-center justify-center gap-4">
    <div class="pt-14">
        <h1 class="text-5xl font-bold mb-4">
            Flag, Manage, Protect with
            <span class="text-[var(--ui-primary)]">
                Custos
            </span>
        </h1>
        <p class="muted-text text-center">
            A highly customizable user-content management system built to prevent unwanted content.
        </p>
        <div class="flex flex-row gap-2 justify-center pt-4">
            <UButton size="xl" label="Get Started" href="#get-started" />
            <UButton size="xl" variant="subtle" label="Test Endpoints" to="/playground" />
        </div>
    </div>
    <NuxtImg src="/hero_pages.png" :placeholder="[16, 9, 85, 10]" class="rounded-lg w-[90%] mt-4"/>
</div>
</template>

<script lang="ts" setup>

</script>

<style>

</style>