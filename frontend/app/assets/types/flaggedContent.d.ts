export type Tag = "toxicity" | "severe_toxicity" | "obscene" | "identity_attack" | "insult" | "threat" | "sexual_explicit";
export type FlaggedContent = {flags: Tag[], content: string};