<template>
    <ConfigLayout>
      <EndpointSummary path="scheduled pipeline" title="Pipeline Check"
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
    </ConfigLayout>
  </template>
  
  <script lang="ts" setup>
  const state = reactive({
      enabled: true,
      check: true
  });
  </script>
  
  <style scoped>
  
  </style>