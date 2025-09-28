<template>
  <div class="p-4 flex gap-4 flex-col">
    <UAlert v-if="failed" color="error" title="Failed to load configs" />
    <ConfigSkeleton v-if="!loaded" />
    <UTabs
      v-if="!failed && loaded" v-model="selectedConfig"
      :items="items" :unmountOnHide="false"
      :ui="{list: '[&>button]:basis-0'}">
      <template #mailValidation>
        <ConfigMailValidation :config="mailValidation!" @submit="submitConfig" />
      </template>
      <template #realtimeCheck>
        <ConfigRealtimeContentCheck :config="realtimeContentCheck!" @submit="submitConfig" />
      </template>
      <template #deepAnalysis>
        <ConfigDeepAnalysis :config="deepAnalysis!" @submit="submitConfig" />
      </template>
      <template #metrics>
        <ConfigMetrics :config="metrics!" @submit="submitConfig" />
      </template>
    </UTabs>
  </div>
</template>

<script lang="ts" setup>
import type { TabsItem } from '@nuxt/ui'
import { TITLE_SUFFIX } from '~/assets/data/appData';
import type { BaseConfig, DeepAnalysisConfig, MailValidationConfig, MetricsConfig, RealtimeContentCheckConfig } from '~/assets/types/configs';

const route = useRoute();
const router = useRouter();
const toast = useToast();
const backend = useBackend();

useHead({
  title: 'Configure Endpoints' + TITLE_SUFFIX
});

const items: TabsItem[] = [
  {
    label: 'Mail Validation',
    icon: 'lucide:mail',
    slot: 'mailValidation'
  },
  {
    label: 'Realtime Content Check',
    icon: 'lucide:clock',
    slot: 'realtimeCheck'
  },
  {
    label: 'Deep Content Analysis',
    icon: 'lucide:brain-circuit',
    slot: 'deepAnalysis'
  },
  {
    label: 'Metrics',
    icon: 'lucide:chart-column',
    slot: 'metrics'
  }
];

const mailValidation = await getConfig<MailValidationConfig>("mail_validation");
const realtimeContentCheck = await getConfig<RealtimeContentCheckConfig>("content_check");
const deepAnalysis = await getConfig<DeepAnalysisConfig>("deep_analysis");
const metrics = await getConfig<MetricsConfig>("metrics");

const loaded = ref(false);
const failed = ref(false);
onBeforeMount(() => {
  failed.value = mailValidation === undefined
                  || realtimeContentCheck === undefined
                  || deepAnalysis === undefined
                  || metrics === undefined;
  
  if (failed.value) {
    showFail("Failed to load config from backend.");
  }
  loaded.value = true;
});

async function getConfig<T extends BaseConfig>(namespace: string) {
  try {
    return await backend.getConfig<T>(namespace);
  } catch {  
    return undefined;
  }
}

async function submitConfig(config: BaseConfig, namespace: string) {
  try {
    const result = await backend.setConfig(namespace, config);
    if (result.code === "OK") {
      showSuccess();
      return
    }
  } catch { /* empty */ }
  showFail("Failed to update config in the backend.");
}

function showSuccess() {
  toast.add({
    title: 'Success',
    description: 'Updated config in the backend.',
    icon: 'lucide-check',
    color: 'success'
  });
}
function showFail(description: string) {
  toast.add({
    title: 'Failed',
    description: description,
    icon: 'lucide-x',
    color: 'error',
    duration: 5000
  });
}

const selectedConfig = computed({
  get() {
    return (route.query.tab as string) || '0';
  },
  set(tab) {
    router.push({
      path: '/config',
      query: { tab },
      // hash: '#'
    })
  }
})
</script>

<style>

</style>