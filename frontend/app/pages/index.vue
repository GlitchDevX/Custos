<template>
    <PagePromo v-if="runtimeConfig.public.promoMode" />
    <PageWelcome v-else />
</template>

<script lang="ts" setup>
const runtimeConfig = useRuntimeConfig();
</script>