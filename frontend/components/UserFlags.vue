<template>
  <div class="flex flex-row gap-2">
    <UBadge
      v-for="({flag, color}, index) in coloredFlags" :key="index"
      :label="flag" :color="color" variant="subtle" />
  </div>
</template>

<script lang="ts" setup>
const props = defineProps({
  flags: {
    type: Array<string>,
    required: true
  }
});

const coloredFlags = computed(() => {
  return props.flags.map((f) => {

    const x = {
      "slurs": 'error' as const,
      "spam": 'warning' as const,
      "harassment": 'error' as const,
      "hate speech": 'error' as const,
      "misinformation": 'info' as const,
      "scams": 'error' as const,
    }[f];
    
    return {flag: f, color: x}
  });
})
</script>

<style scoped>

</style>