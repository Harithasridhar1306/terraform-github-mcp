resource "google_compute_firewall" "allow_http" {
  name    = "allow-http"
  network = var.network

  allow {
    protocol = "tcp"
    ports    = ["80", "443"]
  }

  direction     = "INGRESS"
  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["gke-node"]
}
