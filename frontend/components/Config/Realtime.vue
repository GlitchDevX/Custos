<template>
    <ConfigLayout>
        <EndpointSummary
            path="/check-content" title="Realtime Check"
            summary="This endpoint is used to quickly verify or censor user-content by applying rules." />
        <div>
            <USwitch
                v-model="state.enabled" unchecked-icon="lucide-x" checked-icon="lucide-check"
                label="Endpoint enabled" size="xl" class="pb-8" />

            <div>
                <FeatureToggle
                    v-model="state.urlCheck" title="URL Check"
                    description="Remove and flag valid URLs or IPs." />

                <FeatureToggle
                    v-model="state.blockedWordsCheck" title="Blocked Words Check"
                    description="Remove and flag banned words. This includes profanity." />

                <UFormField
                    label="Extra Banned Words" size="xl" class="pt-4"
                    :class="{'low-opacity': !state.blockedWordsCheck}">
                    <p class="muted-text">
                        Comma separated list of additional words to ban.
                    </p>
                    <UTextarea
                        v-model="state.blockedWords" spellcheck="false" placeholder="enormous, milk..."
                        :maxrows="5" :autoresize="true" class="w-lg mt-1" />
                </UFormField>
            </div>
        </div>
        <UButton label="Save" size="lg" class="mt-8" @click="submitConfig" />
    </ConfigLayout>
</template>

<script lang="ts" setup>
import type { ConfigBody } from '~/assets/types/config/realtimeContentCheck';

const emit = defineEmits<{
    submit: [config: object, namespace: string]
}>();
const props = defineProps({
    config: {
        type: Object,
        required: true
    }
});

const state = reactive({
    enabled: true,
    urlCheck: true,
    blockedWordsCheck: true,
    blockedWords: ""
});

onBeforeMount(() => {
    Object.assign(state, props.config);
    state.blockedWords = props.config["blockedWords"].join(', ');
});

async function submitConfig() {
    const bodyState = { ...state } as ConfigBody;
    bodyState.blockedWords = state.blockedWords.split(', ').map(s => s.trim()).filter(s => s.length > 0);

    emit("submit", bodyState, 'content_check');
}
</script>

<style scoped>

</style>