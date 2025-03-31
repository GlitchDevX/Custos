<template>
  <div class="pt-8">
    <USwitch 
        v-model="model"
        unchecked-icon="lucide-x"
        checked-icon="lucide-check"
        :label="props.title"
        size="xl"
        class="pb-1"
    />
    <p class="muted-text">
        {{props.description}}
    </p>
  </div>
</template>

<script lang="ts" setup>
const model = defineModel<boolean>();
const props = defineProps({
    title: {
      type: String,
      required: true
    },
    description: {
      type: String,
      required: true
    }
});
</script>

<style scoped>

</style>