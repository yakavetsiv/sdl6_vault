---
type: source
title: "sdl-dashboard"
created: 2026-06-05
updated: 2026-06-05
tags:
  - github
  - sdl6
  - dashboard
  - react
  - three-js
  - 3d-map
status: active
repo: AC-SDL6/sdl-dashboard
branch_default: main
related:
  - "[[lab_sensor]]"
  - "[[LabSense Paper Writing Style Profile]]"
---

# sdl-dashboard

**Repo:** [AC-SDL6/sdl-dashboard](https://github.com/AC-SDL6/sdl-dashboard)  
**Stack:** React + TypeScript + Vite + shadcn/ui + Tailwind + FastAPI backend + PostgreSQL  
**Dev port:** 3001 (frontend), 7000 (backend)

---

## PR #7 — Feature: 3D Map Integration (merged 2026-05-17)

**Branch:** `feature/3d-map-integration` → `main`  
**Scope:** 58 files, +6,815 / -3,115 lines  
**Summary:** Integrated interactive 3D lab model (WebGL/React Three Fiber) with backend-backed device-to-position mappings, live camera frustum overlays, sensor markers, and admin management UI.

### What was built

**Backend:**
- `three_map_mappings.py` (263 lines) — full CRUD REST API for device-to-3D-position mappings
- `models/three_map_mapping.py` — SQLAlchemy model: `device_id`, `x/y/z`, `rotation`, `label`, `camera_source`
- `schemas/three_map_mapping.py` — Pydantic schemas (create/update/response)
- Migration `2026-05-16_create_three_map_device_mappings.sql` — new table with FK to devices

**Frontend — `src/features/three-map/`:**
| File | Role |
|------|------|
| `ThreeMapView.tsx` | Entry point; mounts Canvas + Scene |
| `ThreeMapDataBridge.tsx` | Fetches device mappings + sensor readings from API; feeds 3D scene |
| `Scene.tsx` | Root Three.js scene; composes all sub-components |
| `LabModel.tsx` | Loads `sdl6_webgl_v5_draco.glb` (Draco-compressed); handles model visibility |
| `SensorMarkers.tsx` | Renders 3D sensor position markers, click-to-select, hover tooltip |
| `CameraFrustums.tsx` | Visualizes camera FOV frustums at mapped positions |
| `DeviceList.tsx` | Sidebar panel — lists all mapped devices, filter/search, click-to-fly |
| `Sidebar.tsx` | Full sidebar with device detail, live camera feed embed, sensor readings |
| `Toolbar.tsx` | Top toolbar — toggle layers (model/sensors/cameras/labels/frustums) |
| `FlyControls.tsx` | Smooth fly-to-device camera animation |
| `CameraControls.tsx` | Orbit + pan + zoom controls wrapper |
| `DeviceLabels.tsx` | Floating 3D HTML labels for each mapped device |
| `DeviceTooltip.tsx` | Hover tooltip showing device name + last sensor value |
| `ControlsHelp.tsx` | Keyboard/mouse controls help overlay |
| `LoadingScreen.tsx` | Loading spinner while GLB model loads |
| `SceneLighting.tsx` | Ambient + directional lighting setup |
| `config/cameraSources.ts` | Camera stream URL mappings (go2rtc/Frigate sources) |
| `config/devices.ts` | Static device config (fallback when backend mapping absent) |
| `hooks/useDeviceInteraction.ts` | Click/hover interaction state |
| `hooks/useIsMobile.ts` | Responsive breakpoint hook |
| `store/useStore.ts` | Zustand store — selected device, layer visibility, fly target |
| `types/index.ts` | ThreeMapDevice, SensorMarker, CameraFrustum types |

**Admin:**
- `AdminThreeMapMappings.tsx` (312 lines) — full CRUD admin table: add/edit/delete device-to-position mappings, select device from dropdown, set x/y/z/rotation, assign camera source

**Assets:**
- `public/models/sdl6_webgl_v5_draco.glb` — Draco-compressed 3D lab model (Git LFS)
- `public/lovable-uploads/sdl6-default-map-v7.svg/png` — 2D fallback floor plan

### Key design decisions
- React Three Fiber (`@react-three/fiber`) + Drei (`@react-three/drei`) for declarative Three.js
- Draco compression on GLB for fast web load
- Backend mappings allow admin to position any device in 3D without code changes
- Camera frustums dynamically rendered from the same mapping data as sensor markers
- Zustand store keeps fly-to and selection state; avoids prop-drilling through deep component tree
- `ThreeMapDataBridge` polls API on mount; no WebSocket (polling acceptable for device positions which rarely change)

### Sonar issues resolved post-merge
- Removed JSX transparent material props in React Three Fiber (Sonar flagged as React incompatible)
- Replaced `window`/`document` globals with `globalThis` for SSR safety
- Split `RobotCameraStream.tsx` (1465 lines touched) to reduce cyclomatic complexity

---

## Active Branch: feature/sensor-monitor (not yet merged)

**PR:** https://github.com/AC-SDL6/sdl-dashboard/pull/new/feature/sensor-monitor  
**Purpose:** LabSense physical-state sensor dashboard mockup

**Files added:**
- `frontend/src/pages/labsense/LabSenseDashboard.tsx` — 3-tier sensor monitor page
- `frontend/src/data/labsenseMockData.ts` — mock deployment data (280,525 readings)

**Route:** `/labsense`  
**Data:** static mock (no live DB); connects to TimescaleDB via `/api/labsense/*` when backend is connected  
See [[LabSense Paper Writing Style Profile]] for deployment context.

---

## Other notable PRs

| PR | Description | Merged |
|----|-------------|--------|
| #19 | refactor: imaging + image browser split | 2026-06 |
| #18 | refactor: imaging + visualization split | 2026-06 |
| #11 | Snyk security fix | 2026-05 |
| #4 | Snyk security fix | 2026-05 |

---

## Dev setup

```bash
# Frontend (port 3001)
cd frontend && npm install && npm run dev

# Backend (port 7000)
cd backend && uvicorn app.main:app --reload --port 7000

# Full stack
npm run dev  # from root (runs both concurrently)
```

Auth: password `admin123` (dev fallback; set `VITE_AUTH_STRING` env var in production)
