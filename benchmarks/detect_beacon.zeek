event http_request(c: connection, method: string, original_URI: string, unescaped_URI: string, version: string)
{
    if (/beacon/ in original_URI)
        print fmt("🔍 Beacon detected: %s -> %s at %s",
                  c$id$orig_h, c$id$resp_h, network_time());
}
