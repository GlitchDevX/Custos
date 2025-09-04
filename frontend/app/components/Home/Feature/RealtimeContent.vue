<template>
    <div class="flex justify-center items-center">
        <div class="w-3xl max-w-full">
            <div class="max-w-xl">
                <h2 class="text-3xl font-bold">
                    Realtime Profanity Check
                </h2>
                <p class="muted-text">
                    Remove profanity and spam from user content to improve community health.
                </p>
            </div>
            <div class="flex flex-col mt-2">
                <div class="flex justify-start">
                    <CodeBlock :content="JSON.stringify(realtimeInput, null, 4)" language="json" />
                </div>
                <div class="flex justify-center">
                    <UIcon class="sm:-rotate-45" name="lucide-arrow-down" :size="50" />
                </div>
                <div class="flex justify-end">
                    <CodeBlock :content="JSON.stringify(realtimeOutput, null, 4)" language="json" />
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>
const realtimeInput = {
    "content": "Ayo bro fuck you! Also visit my website: https://sapphire-games.com"
}
const realtimeOutput = {
    "tags": ["profanity", "spam"],
    "censored": "Ayo bro **** you! Also visit my website: *************************"
}
</script>

<style>

</style>