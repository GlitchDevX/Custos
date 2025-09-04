<template>
    <div class="p-4 flex gap-16 flex-col">
        <HomeHero />
        <HomeFeatureMailValidation />
        <HomeFeatureRealtimeContent />
        <HomeFeatureDeepCheck />
        <HomeFeatureConfigurable/>
        <HomeGetStarted />
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