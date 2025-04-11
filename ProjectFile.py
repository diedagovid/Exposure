from pathlib import Path

# Define project structure
project_root = Path("/mnt/data/VACU-Exposure-Language")
readme_path = project_root / "README.md"
demo_expg_path = project_root / "examples" / "hello_world.expg"

# README content (shortened here for clarity)
readme_content = """# Exposure Language

> A precise, expressive programming language for distributed capsules, nodes, events...
[...truncated for brevity in code...]
— _Joey Soprano, 2025_
"""

# Sample Exposure demo file
demo_expg_content = """// Hello World Capsule in Exposure Language

capsule HelloWorldCapsule {
  node Greeter {
    string message = "Hello, Exposure World!";
    
    render_frame() {
      call("display", message);
    }

    suggest() {
      call("autoplay");
    }
  }

  hook(freq@=2s) {
    call("heartbeat");
  }
}
"""

# Create folder structure and write files
(project_root / "examples").mkdir(parents=True, exist_ok=True)
readme_path.write_text(readme_content)
demo_expg_path.write_text(demo_expg_content)

str(project_root)  # Return path for user access

from pathlib import Path

# Recreate project structure after environment reset
project_root = Path("/mnt/data/VACU-Exposure-Language")
readme_path = project_root / "README.md"
demo_expg_path = project_root / "examples" / "hello_world.expg"

# Full README content
readme_content = """# Exposure Language

**Exposure** is a next-gen programming language tailored for distributed systems, real-time reactive control, and multi-node capsules within the Violet Aura Creations Universe (VACU). It is designed for building intelligent, fault-resilient systems with embedded AI suggestion blocks, blockchain-style audit trails, GUI rendering, and node-grid synchronizations.

---

## ✨ Features

### 🔤 Grammar

- **Strongly-typed**: Types include `int`, `float`, `bool`, `char`, `void`, `node`, `capsule`, `stream`, `event`, `chain`, `hook`, `trigger`.
- **Capsule-driven**: Units of deployable logic containers.
- **Multi-node distribution** via `node.render` and `nodegrid.sync`.
- **Trigger hooks**: Time-based or condition-based execution.
- **AI-powered suggest() blocks**: Recommends next action using embedded reasoners.
- **Immutable blockchain logs**: `CAPSULE.sign(...)` for audit trails.
- **Adaptive GUI Theming**: Dark/light styling based on health state.
- **Error handling**: Panic triggers, `await until`, diagnostics.
- **Concurrency**: `async`, `multithread`, `sandboxed register on chip`.

---

## 📘 Language Syntax

```expg
capsule ExampleCapsule {
  node Sensor {
    int reading = 0;

    render_frame() {
      call("update_display", reading);
    }

    suggest() {
      if (reading > 75) call("activate_cooling");
    }
  }

  hook(freq@=3s) {
    call("collect_data");
  }

  stream logEvent(int id, string msg) {
    call("write_log", id, msg);
  }

  CAPSULE.sign(logEvent, immutable=true);
}

