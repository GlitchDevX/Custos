<template>
    <ConfigLayout>
        <EndpointSummary 
            path="/check-content" title="Realtime Check"
            summary="This endpoint is used to quickly verify or censor user-content by applying rules."
        />
        <USwitch
            v-model="state.enabled"
            unchecked-icon="lucide-x"
            checked-icon="lucide-check"
            label="Endpoint enabled"
            size="xl"
            class="pb-8"
        />
        
        <div>
            <FeatureToggle
                v-model="state.urlCheck"
                title="URL Check"
                description="Remove and flag valid URLs or IPs."
            />
            
            <FeatureToggle
                v-model="state.blockedWordsCheck"
                title="Blocked Words Check"
                description="Remove and flag banned words. This includes profanity."
            />

            <UFormField label="Extra Disposable Domains" size="xl" class="pt-4" :class="{'low-opacity': !state.blockedWordsCheck}">
                <p class="muted-text">
                    Comma separated list of additional domains to mark as disposable.
                </p>
                <UTextarea
                    v-model="state.blockedWords"
                    spellcheck="false"
                    placeholder="enormous, milk..."
                    :maxrows="5" :autoresize="true" class="w-lg mt-1" />
            </UFormField>


        </div>
    </ConfigLayout>
</template>

<script lang="ts" setup>
const state = reactive({
    enabled: true,
    urlCheck: true,
    blockedWordsCheck: true,
    blockedWords: ""
});
</script>

<style scoped>

</style>