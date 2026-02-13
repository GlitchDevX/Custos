export interface BaseConfig {
  enabled: boolean;
}

export interface MailValidationConfig extends BaseConfig {
  disposableCheck: boolean;
  disposableDomains: string[];
  formatCheck: boolean;
  maxHeloChecks: number;
  mxRecordCheck: boolean;
  smtpHelo: boolean;
}

export interface RealtimeContentCheckConfig extends BaseConfig {
  blockedWordsCheck: boolean;
  blockedWords: string[];
  urlCheck: boolean;
}

export interface DeepAnalysisConfig extends BaseConfig {
  threshold: number;
  labelsToExclude: string[];
}

// eslint-disable-next-line @typescript-eslint/no-empty-object-type
export interface MetricsConfig extends BaseConfig { }

