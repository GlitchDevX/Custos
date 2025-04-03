export type Tag = "slurs" | "spam" | "harassment" | "hate speech" | "misinformation" | "scams";
export type FlaggedUser = {id: string, username: string, flags: Tag[], message: string}; 