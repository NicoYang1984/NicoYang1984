<div align="center">
  <img src="assets/cover.svg" alt="Build · Research · Create — AI systems, open source, music and beyond" width="100%" />
  <br /><br />
  <img src="https://avatars.githubusercontent.com/u/103879136?v=4" width="88" height="88" alt="Nico's current GitHub avatar" />
</div>

# Ziyang Liang · 梁子洋

**Call me Nico. I build AI systems, ask research questions, and make music.**

I'm interested in what makes an agent's work dependable: how it uses tools, manages state, checks its outputs, and communicates what is actually finished. Away from code, I explore ideas through music production and writing.

把系统做可靠，把想法变成作品。这里记录我的工程实践、研究探索，也留给音乐与日常创作。

[Engineering](#engineering--open-source) · [Research](#research--independent-projects) · [Music](#music--creative-work) · [Elsewhere](#elsewhere)

## A little background

- **HKUST (Guangzhou)** — Master's, Data-Centric AI Technology · 香港科技大学（广州）
- **South China Normal University** — Bachelor's, Software Engineering · 华南师范大学
- **Current interests** — Agent Runtime, reliability, LLM evaluation, model alignment, and open-source collaboration.

## Engineering & open source

I care about the gap between an agent reaching its final state and a task delivering its intended result.

### Merged into LazyMind

- **[SubAgent completion contracts · #750](https://github.com/LazyAGI/LazyMind/pull/750)** — Validate required artifacts and their types before accepting completion, with structured failure reporting and cancellation checks.
- **[Terminal state reconciliation · #748](https://github.com/LazyAGI/LazyMind/pull/748)** — Preserve accepted business outcomes when a stream later fails, while retaining transport diagnostics.
- **[Superpowers dispatch reliability workflow · #852](https://github.com/LazyAGI/LazyMind/pull/852)** — A reusable example of brief gates, inspectable artifacts, and review checkpoints; includes missing-brief fault injection.

### In progress · not merged

- **[LazyMind compatibility trial · #873](https://github.com/LazyAGI/LazyMind/pull/873)** — **Draft.** A Competitive Brief Skill-to-Workflow trial and portable package, documenting execution failures and assisted recovery.
- **[FastMCP schema defaults · #6134](https://github.com/PrefectHQ/fastmcp/pull/6134)** — **Draft.** A proposed fix for incompatible defaults during dataclass hydration.

<sub>Selected PR states checked on 2026-10-29. Each link opens the live upstream record.</sub>

## Research & independent projects

**[Superpowers · completion evidence experiment](https://github.com/NicoYang1984/superpowers-2451-completion-evidence)**<br />
An independent, agent-assisted study of final-report evidence across 30 model sessions. The observed improvement concerns report auditability; the tested model did not reproduce the original false-completion behavior. Public protocol, fixtures, scores, and limitations are included. No upstream PR was submitted.

**[EcomAlign-Qwen](https://github.com/NicoYang1984/EcomAlign-Qwen)**<br />
An e-commerce post-training pipeline with a completed Qwen2.5-1.5B path: synthetic data, LoRA SFT, DPO, rule-based evaluation, and vLLM serving evidence.

**[DPO + PairRM alignment](https://github.com/NicoYang1984/assignment4-dpo-pairrm)**<br />
A course project using Qwen2.5-7B, PairRM preferences, and LoRA DPO. A small-scale study with 40 training pairs and 10 held-out prompts, with qualitative comparisons.

**[Company relation graph study](https://github.com/NicoYang1984/llm-enhanced-stock-prediction-graph)**<br />
An empirical project comparing text, numerical features, and company-relation graphs for next-quarter classification, with temporal splits and published baseline results.

**[Financial news sentiment notebook](https://github.com/NicoYang1984/Financial-News-Sentiment-Analyzer)**<br />
A course-built analysis tool exploring Naive Bayes, LSTM, and BERT approaches to financial headline sentiment in a public notebook.

## Music & creative work

Music is another way I explore structure, texture, and feeling. Alongside engineering and research, I make room for producing music, writing, and following an idea into something tangible.

**[Listen on NetEase Cloud Music / 网易云音乐人主页 ↗](https://music.163.com/#/artist?id=53437311)**

写代码之外，也写旋律、写文字。希望这里慢慢长成一个有作品、有声音，也有生活的空间。

<!-- MUSIC_WORKS: Add verified track titles and public listening links when ready. -->

<!-- PHOTO_GALLERY_START
Reserved for 2–3 real, authorized photos. Activate each image only after its file exists.
Use stacked images for comfortable mobile reading; see PHOTO_GUIDE.md.

### Notes from life / 创作与日常

<img src="assets/photos/music-studio.jpg" width="560" alt="Nico making music in the studio" />

<img src="assets/photos/creative-work.jpg" width="560" alt="A moment from Nico's creative work" />

<img src="assets/photos/everyday.jpg" width="560" alt="A moment from Nico's everyday life" />
PHOTO_GALLERY_END -->

## Elsewhere

[GitHub](https://github.com/NicoYang1984) · [NetEase Cloud Music / 网易云音乐](https://music.163.com/#/artist?id=53437311)

<details>
<summary>More places, over time / 更多平台，慢慢补齐</summary>

Douyin / 抖音 · Bilibili / B 站 · Zhihu / 知乎 · Other music platforms / 其他音乐平台 · Personal website / 个人网站

Links will appear here as I add my public profiles.

<!-- SOCIAL_LINKS: Replace the plain-text platform names only with confirmed public profile URLs. -->

</details>

---

<div align="center"><sub>Build things carefully. Create things freely.</sub></div>
