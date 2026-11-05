---
title: "Accessibility statement"
label: "Accessibility"
permalink: /accessibility/
ref: accessibility
---

Mälardalen University is responsible for this website. We want as many
people as possible to be able to use it. This page describes how the website
complies with the Swedish Act (2018:1937) on accessibility to digital public
services, which accessibility problems we know about, and how you can report
shortcomings so that we can fix them.

## How accessible is the website?

We know that parts of the website are not fully accessible. See the section
on non-accessible content below.

## What can you do if you cannot use parts of the website?

If you need content from the website in a different format, you can contact us.
{% if site.accessibility_contact != "" %}Email
[{{ site.accessibility_contact }}](mailto:{{ site.accessibility_contact }}).{% endif %}

## Report accessibility problems

We are always working to improve the accessibility of the website. If you
find problems that are not described on this page, or if you think we do not
meet the requirements of the law, please let us know so that we know the
problem exists.{% if site.accessibility_contact != "" %} Email
[{{ site.accessibility_contact }}](mailto:{{ site.accessibility_contact }}).{% endif %}

## Enforcement

The Agency for Digital Government (Digg) is responsible for enforcing the act
on accessibility to digital public services. If you are not satisfied with how
we handle your comments, you can
[contact Digg and tell them](https://www.digg.se/tdosanmalan).

## Technical information about the website's accessibility

The website is partially compliant with the act on accessibility to digital
public services, due to the shortcomings described below. We assess the
website against WCAG 2.2 level AA, which includes the requirements of
WCAG 2.1 AA and the European standard EN 301 549.

## Non-accessible content

### Non-compliance with the requirements

- **Videos.** The videos about AutoBike and AutoSail are shown via YouTube. We
  have not yet checked that they have correct subtitles or a text alternative
  describing the content (WCAG 1.2.1, 1.2.2 and 1.2.5). We are working on
  fixing this.
- **Publication list.** The list is fetched automatically from DiVA. Titles in
  languages other than the page language are not marked with the correct
  language, so a screen reader may pronounce them incorrectly (WCAG 3.1.2).

## How we tested the website

We have carried out a self-assessment (internal testing) of the website, with
both automated tools (axe-core) and manual review of colour contrast, keyboard
navigation, language markup, heading structure and display on narrow screens.

The most recent assessment was made on 3 November 2026.

This statement was last updated on 3 November 2026.
