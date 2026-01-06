<template>
  <UContainer class="min-h-[calc(100dvh-64px)] flex flex-col justify-between">
    <div class="grow flex justify-center items-center">
      <UPageCard title="Legal Notice" :ui="{ title: 'text-2xl text-primary'}">
        <template #description>
          <h2 class="text-lg font-bold text-default">
            Responsible for content
          </h2>
          <p>
            Jonas Ringeis<br>
            Steinbeker Hauptstraße 193<br>
            22115 Hamburg<br>
            Germany<br>
            <br>
            <span class="text-default">
              Email:<br>
            </span>
            <a class="inline-link" href="mailto:contact@glitchdev.me" target="_blank">contact@glitchdev.me</a>
          </p>
        </template>
      </UPageCard>
    </div>

    <NavFooter />
  </UContainer>
</template>

<script lang="ts" setup>
useSeoMeta({
  robots: {
    noindex: true
  }
})
</script>

<style>

</style>