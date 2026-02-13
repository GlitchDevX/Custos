<template>
  <UCollapsible v-model:open="model" :arrow="true" class="group">
    <UButton block label="Show Response" variant="ghost" leading-icon="lucide-chevron-down"
      :ui="{ leadingIcon: 'group-data-[state=open]:rotate-180 transition-transform duration-200' }" />
    <template #content>
      <CodeBlock :content="JSON.stringify(content, null, 4)" language="json" />
    </template>
  </UCollapsible>
</template>

<script lang="ts" setup>

defineProps({
  content: {
    type: Object,
    required: true
  }
});

const model = defineModel({
  type: Boolean
});
</script>

<style></style>