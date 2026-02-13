<template>
    <ConfigLayout>
        <EndpointSummary
            path="/check-content" title="Realtime Check"
            summary="This endpoint is used to quickly verify or censor user-content by applying rules." />
        <div>
            <USwitch 
                v-model="state.enabled" unchecked-icon="lucide-x" checked-icon="lucide-check"
                label="Endpoint enabled" size="xl" class="pb-8" />

            <div :class="{ 'low-opacity': !state.enabled }">
                <FeatureToggle 
                    v-model="state.urlCheck" title="URL Check"
                    description="Remove and flag valid URLs or IPs." />

                <FeatureToggle 
                    v-model="state.blockedWordsCheck" title="Blocked Words Check"
                    description="Remove and flag banned words. This includes profanity." />

                <UFormField 
                    label="Extra Banned Words" size="xl" class="pt-4"
                    :class="{ 'low-opacity': !state.blockedWordsCheck }">
                    <p class="muted-text">
                        List of additional words to ban. You can insert a comma-separated list.
                    </p>
                    <UInputTags
                        v-model="state.blockedWords" :addOnPaste="true" class="mt-1 w-full"
                        :spellcheck="false" />
                </UFormField>
            </div>
        </div>
        <UButton label="Save" size="lg" class="mt-8" @click="submitConfig" />
    </ConfigLayout>
</template>

<script lang="ts" setup>
import { UInputTags } from '#components';
import type { RealtimeContentCheckConfig } from '~/assets/types/configs';

const emit = defineEmits<{
    submit: [config: RealtimeContentCheckConfig, namespace: string]
}>();
const props = defineProps({
    config: {
        type: Object as PropType<RealtimeContentCheckConfig>,
        required: true
    }
});

const state = reactive<RealtimeContentCheckConfig>({
    enabled: true,
    urlCheck: true,
    blockedWordsCheck: true,
    blockedWords: []
});

onBeforeMount(() => {
    Object.assign(state, props.config);
});

async function submitConfig() {
    emit("submit", state, 'content_check');
}
</script>

<style scoped></style>