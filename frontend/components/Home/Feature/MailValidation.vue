<template>
    <div class="flex justify-center items-center">
        <div class="w-3xl">
            <div class="max-w-xl">
                <h2 class="text-3xl font-bold">
                    Powerful Mail Validation
                </h2>
                <p class="muted-text">
                    Advanced mutli-step mail verification to decrease mail bounces and keep mail reputation.
                </p>
            </div>
            <div class="flex flex-row justify-end pt-2">
                <UStepper :items="mailValidationSteps" class="max-w-2xl" />
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>
import type { StepperItem } from '@nuxt/ui';

const mailValidationSteps = [
    {
        title: 'Format Validation',
        description: 'Basic formatting checks',
        icon: 'lucide-regex'
    },
    {
        title: 'Disposable Filter',
        description: 'Filter out disposable emails',
        icon: 'lucide-trash-2'
    },
    {
        title: 'Mailserver Check',
        description: 'Perform advanced mailserver checks',
        icon: 'lucide-server-crash'
    }
] as StepperItem[]
</script>

<style>

</style>