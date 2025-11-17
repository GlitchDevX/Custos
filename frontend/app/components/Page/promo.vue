<template>
    <div class="p-4 pb-0 flex gap-16 flex-col">
        <HomeHero />
        <HomeFeatureMailValidation />
        <LazyHomeFeatureRealtimeContent hydrate-on-visible />
        <LazyHomeFeatureDeepCheck hydrate-on-visible />
        <LazyHomeFeatureConfigurable hydrate-on-visible/>
        <LazyHomeFeatureMetrics hydrate-on-visible />
        <LazyHomeGetStarted hydrate-on-visible />
        <LazyNavFooter hydrate-on-visible />
    </div>
</template>

<script lang="ts" setup>
import { TITLE_SUFFIX } from '~/assets/data/appData';

useHead({
    title: 'Home' + TITLE_SUFFIX
});
</script>

<style scoped>

</style>