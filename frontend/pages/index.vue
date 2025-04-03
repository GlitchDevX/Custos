<template>
    <div class="p-4 flex gap-4 flex-col">
        <HomeHero />
        <HomeFeatureMailValidation class="pt-8" />
        <HomeFeatureRealtimeContent class="pt-8" />
        <HomeFeaturePipeline class="pt-8" />
        <HomeFeatureGetStarted class="pt-8" />
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