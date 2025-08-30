import type { BaseConfig } from "./baseConfig";

export interface MailValidationConfig extends BaseConfig {
    disposableCheck: boolean;
    disposableDomains: string[];
    enabled: boolean;
    formatCheck: boolean;
    maxHeloChecks: number;
    mxRecordCheck: boolean;
    smtpHelo: boolean;
}