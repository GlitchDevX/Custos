<template>
  <ProseCodeCollapse>
    <ProsePre filename="dashboard.json" language="json">
        {{ grafanaDashboard }}
    </ProsePre>
  </ProseCodeCollapse>
</template>

<script lang="ts" setup>
import { ProseCodeCollapse } from '#components';
import grafanaDashboard from '~/assets/data/metric-configs/grafana-dashboard.json?raw'
</script>

<style>

</style>