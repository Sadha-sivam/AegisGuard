// Upsell CTAs point at the UPSTREAM Strix Cloud service (app.strix.ai).
// AegisGuard does not host these services; links are optional third-party.
export const SIGNUP_URL = "https://app.strix.ai/api/auth/signup";
export const DEMO_URL = "https://strix.ai/demo";
export const PRICING_URL = "https://strix.ai/pricing";
export const UPSTREAM_CLOUD_HOME = "https://app.strix.ai";

// Attribution params appended to every outbound CTA link so the destination
// analytics can see the local viewer drove the click, with utm_content carrying
// the CTA slug so we know which one.
const CTA_PARAMS =
  "ref=aegisguard_viewer&utm_source=aegisguard_viewer&utm_medium=local_viewer&utm_campaign=aegisguard_viewer";

export function ctaUrl(base: string, slug: string): string {
  const sep = base.includes("?") ? "&" : "?";
  return `${base}${sep}${CTA_PARAMS}&utm_content=${encodeURIComponent(slug)}`;
}

export function track(event: string, props: Record<string, string | undefined> = {}): void {
  try {
    const body: Record<string, string> = { event };
    for (const [key, value] of Object.entries(props)) {
      if (value !== undefined) body[key] = value;
    }
    const payload = JSON.stringify(body);
    if (typeof navigator !== "undefined" && navigator.sendBeacon) {
      navigator.sendBeacon("/api/event", payload);
    } else {
      void fetch("/api/event", { method: "POST", body: payload, keepalive: true });
    }
  } catch {
    /* analytics is best-effort */
  }
}

export function trackCta(cta: string, surface?: string): void {
  track("cta_clicked", { cta, surface });
}
