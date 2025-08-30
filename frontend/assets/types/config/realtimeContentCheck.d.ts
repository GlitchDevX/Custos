import type { BaseConfig } from "./baseConfig";

export interface RealtimeContentCheckConfig extends BaseConfig {
    blockedWordsCheck: boolean;
    blockedWords: string[];
    urlCheck: boolean;
}