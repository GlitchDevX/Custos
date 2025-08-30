import type { BaseConfig } from "./baseConfig";

export interface RealtimeContentCheckConfig extends BaseConfig {
    enabled: boolean;
    blockedWordsCheck: boolean;
    blockedWords: string[];
    urlCheck: boolean;
}