// Minimal Rust library for AI core (placeholder)

#[cfg(target_arch = "wasm32")]
pub fn noop() -> &'static str {
    "wasm noop"
}

#[cfg(not(target_arch = "wasm32"))]
pub fn compute_heavy(x: i32) -> i32 {
    // placeholder for heavy computation
    x * x
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_compute_heavy() {
        assert_eq!(compute_heavy(3), 9);
    }
}
