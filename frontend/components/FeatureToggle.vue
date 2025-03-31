<template>
  <div class="pt-8">
    <USwitch 
        unchecked-icon="lucide-x"
        checked-icon="lucide-check"
        default-value
        :label="props.title"
        size="xl"
        class="pb-1"
        v-model="model"
    />
    <p class="muted-text">
        {{props.description}}
    </p>
  </div>
</template>

<script lang="ts" setup>
const model = defineModel<boolean>();
const props = defineProps({
    title: String,
    description: String
});
</script>

<style scoped>

</style>