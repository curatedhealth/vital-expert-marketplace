# VITAL plugins for Cowork

This is the marketplace a buyer adds in Cowork. The plugin is free to install. The Digital Health Library key is the purchase.

## Install Evidence and Reimbursement

1. In Cowork, open **Customize**, then **Plugins**, then **Add marketplace**.
2. Enter `curatedhealth/vital-expert-plugins`. Do not paste a file link.
3. Install **Evidence and Reimbursement**.
4. Paste the `vlib_` key when Cowork asks for the Digital Health Library key.
5. Leave the plugin switched on.

The connector address is `https://mcp.vital.expert/api/mcp/library`. Do not install a second market-access connector, and do not create a second key.

## What the buyer does next

Ask for the pack. It opens on three cores: Clinical Validation & Evidence, Health Economics & Value Demonstration, and Market Access & Reimbursement. Choose one core, then one job. The job loads one task. A task calls the library only when that task names a tool. A missing fact stays a gap.

Finding an expert is free. Downloading one expert spends one call on the same key. A successful tool call spends one unit of the monthly cap. Verify can spend several units on one task. When the cap is reached, or the purchase ends, the tools stop. The installed plugin stays.

## What is not in this repository

The key is not in this repository. A person without a key can install the plugin and cannot retrieve library data.
The skills run only while the Digital Health Library connector is connected. Turning the plugin off removes the skills and the connector together. If the connector is not connected, the pack does not answer.

## Regulatory Strategy and Submissions

Same marketplace. Same `vlib_` key. Same connector. Install **Regulatory Strategy and Submissions** beside Evidence and Reimbursement.

It opens on four headings: AI/ML Regulatory, Global Harmonization, Regulatory Strategy, and Submission Excellence. Choose one heading, then one job. The job loads one task.

The library tools in this pack search devices, open one authorization, compare authorizations, read market status, classify a product, read pathway precedents, find United States predicates, watch a register, read what that watch recorded, search safety events, list the loaded registers, retrieve stored guidance, and generate a pathway report. get_deltas is the same call as reading register changes.
The skills run only while the Digital Health Library connector is connected. Turning the plugin off removes the skills and the connector together.
