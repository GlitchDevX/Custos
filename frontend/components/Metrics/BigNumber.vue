<template>
  <div>
    <UCard class="min-w-[250px] metric-card" :class="{'animate-metric': animating}">
      <div class="relative flex items-start flex-col">
        <span class="metric-title">{{ props.title }}</span>
        <span class="text-5xl font-bold">{{ displayedNumber }}</span>
      </div>
    </UCard>
  </div>
</template>

<script lang="ts" setup>
const props = defineProps({
  title: {
    type: String,
    required: true
  },
  number: {
    type: Number,
    required: true
  },
  animationDelay: {
    type: Number,
    default: 0
  }
});

onMounted(() => {
  setTimeout(startNumberAnimation, props.animationDelay * 1000)
});

const animating = ref(false);
const displayedNumber = ref(0);
function startNumberAnimation() {
  if (props.number === 0) {
    animateZero();
    return;
  }

  let stepSize = props.number / 50;
  if (stepSize < 1) {
    stepSize = 1;
  }
  stepSize = Math.round(stepSize * 10) / 10;
  
  animating.value = true;
  animateNumberRec(stepSize);
}
function animateNumberRec(stepSize: number) {
  displayedNumber.value += stepSize;
  displayedNumber.value = Math.round(displayedNumber.value * 10) / 10;
  
  if (displayedNumber.value >= props.number) {
    displayedNumber.value = props.number;
    animating.value = false;
    return;
  }

  setTimeout(animateNumberRec, 1000 / 60, stepSize); //20 updates a second
}
function animateZero() {
  animating.value = true;
  setTimeout(() => animating.value = false, 300);
}
</script>

<style scoped>
.metric-card {
  transition: 0.9s ease;
}
.metric-title {
  color: var(--ui-text-muted);
  position: relative;
}
.animate-metric {
  background: var(--ui-bg-accented);
  transition: 0.3s ease;
}
</style>