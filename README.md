# meichuhackathon_workshop
2022 梅竹黑客松工作坊
---
```
                  ┌────────────────────────────────────────────────┐       ┌────────────────────────────────────────┐
                  │                                                │       │                                        │
                  │ Heroku                                         │       │   Google Cloud Platform (GCP)          │
                  │                                                │       │                                        │
                  │                                                │       │                                        │
                  │                     RESTful                    │       │  ┌────────────────┐ ┌──────────────┐   │
   xxxxx          │     ┌──────────────┐        ┌─────────────┐    │       │  │ inerence       │ │ training     │   │
  x    x          │     │ UI           ├───────►│ API         │    │       │  │                │ │              │   │
   xxxx           │     │              │        │             └────┼───────►──┤Model as service│ │              │   │
 xxxxxx  ─────────┼────►│              │        │             ◄────┼───────┬──┤                │ │              │   │
xx  x xx          │     │              │◄───────┤             │    │       │  └────────────────┘ └──────────────┘   │
    x    ◄────────┼─────┤              │        │             │    │       │                                        │
  xxxx            │     └──────────────┘        └───────┬─────┘    │       │                      ┌─────────────┐   │
 xx   xx          │                                     │          │       │                      │ dataset     │   │
                  │                                     │          │       │                      └─────────────┘   │
                  │                                     │          │       │                                        │
                  └─────────────────────────────────────┼──────────┘       └────────────────────────────────────────┘
                                                        │
                              ┌────────────┬────────────┤
                              │            │            │
                  ┌───────────┼────────────┼────────────┼──────────┐
                  │           │            │            │          │
                  │ MongoDB   │            │            │          │
                  │           │            │            │          │
                  │           │            │            │          │
                  │  ┌────────▼──┐ ┌───────▼────┐ ┌─────▼──────┐   │
                  │  │           │ │            │ │            │   │
                  │  │  pod 1    │ │   pod 2    │ │  pod 3     │   │
                  │  │           │ │            │ │            │   │
                  │  └───────────┘ └────────────┘ └────────────┘   │
                  │                                                │
                  │                                                │
                  └────────────────────────────────────────────────┘
```


1. 建立virtual env (Optional)
- python -m venv alert-sender
- activate.bat

2. 安裝套件
pip install uvicorn
pip install fastapi

3. 安裝heroku CLI
https://devcenter.heroku.com/articles/heroku-cli

4. model weughts 下載，並放置在model/yolov3-obj_v1.weights
https://drive.google.com/file/d/1PtL0wfcyOBZ4CbgxKGoCaA2eVV_kwE6L/view?usp=sharing

