# Maintaining this profile

The public `NicoYang1984/NicoYang1984` repository displays its root `README.md` on the account Overview. Keep the repository public and the README on its default branch.

## Editing

- `README.md`: profile prose, selected work and social links.
- `assets/cover.svg`: original vector banner; no external fonts or scripts.
- `PHOTO_GUIDE.md`: reserved portrait/gallery paths and publishing instructions.
- `scripts/check_profile.py`: standard-library check of active links, local image files, anchors and SVG XML. HTML comments are ignored.

## Contribution records

States were checked against GitHub on **2026-10-29**:

| Contribution | State | Evidence |
| --- | --- | --- |
| LazyMind #750 | Merged 2026-09-29 | https://github.com/LazyAGI/LazyMind/pull/750 |
| LazyMind #748 | Merged 2026-09-28 | https://github.com/LazyAGI/LazyMind/pull/748 |
| LazyMind #852 | Merged 2026-10-21 | https://github.com/LazyAGI/LazyMind/pull/852 |
| LazyMind #873 | Open, Draft | https://github.com/LazyAGI/LazyMind/pull/873 |
| FastMCP #6134 | Open, Draft | https://github.com/PrefectHQ/fastmcp/pull/6134 |

The repository-level Contributor list also includes LazyRAG (merged #8, #10, #22, #25) and kyrolabs/awesome-agents (merged #895), verified through public GitHub PR search on 2026-10-29.

Project descriptions were checked against their public repository READMEs. Education and creative interests follow the account owner's supplied information. No degree dates, publication claims, employment titles, or musical releases were inferred.

When editing, recheck PR metadata rather than inferring merge status from a PR description or closed state. Keep the profile organized by repository and role, not by individual PR. Use an unqualified Contributor label for repositories with merged contributions; describe unmerged submissions as proposed contributions. Keep detailed evidence here rather than expanding the profile with each new PR. Keep independent experiments distinct from accepted upstream work. Verify public visibility before adding any repository.

## Validate and publish

```sh
python3 scripts/check_profile.py
python3 scripts/check_profile.py --online
git diff --check
git diff
git add README.md assets/cover.svg PHOTO_GUIDE.md MAINTENANCE.md scripts/check_profile.py .gitignore
git commit -m "Update personal profile"
git push origin main
```

The optional HTTP check reports blocked or timed-out pages for manual verification; HTTP 200 alone does not prove the identity or content of an external profile. NetEase uses client-side routing and may require a normal browser or its app. Check the artist ID `53437311` when updating music links.

After publishing, check the account Overview on desktop and mobile. Keep images fluid, avoid wide tables in the profile, and add only real photo files. The initial design uses plain links instead of third-party badge or statistics services.
