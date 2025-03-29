<template>
    <div class="px-40 py-8">
      <EndpointSummary path="/report-content" title="Realtime Check"
          summary="This endpoint is used to quickly verify or censor user-content by applying rules."
      />
      <USwitch
          unchecked-icon="lucide-x"
          checked-icon="lucide-check"
          label="Endpoint enabled"
          size="xl"
          class="pb-8"
          v-model="state.enabled"
      />
  
      <div>
          <FeatureToggle
              title="Some Check"
              description="Placeholder description. Yoyoyo."
              v-model="state.check"
          />
      </div>
    </div>
  </template>
  
  <script lang="ts" setup>
  const state = reactive({
      enabled: true,
      check: true
  });
  </script>
  
  <style scoped>
  
  </style>