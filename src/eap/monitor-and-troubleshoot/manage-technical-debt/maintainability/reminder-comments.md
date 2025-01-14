---
summary: A comment is set as a reminder. Reminder comments may indicate important technical debt or unresolved issues.
tags: technical debt, reminder comments, task management, comment properties, issue tracking
guid: 24d9c5d6-b735-4e64-b47f-ada091e94f1f
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/IStE4rx9SlrBLEK5OXk4nm/Monitor-and-troubleshoot-apps?node-id=3611-10&t=stw8ZZ271Tgj8Y4g-1
coverage-type:
  - unblock
  - remember
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
---
# Reminder comments

A comment is set as a reminder. 

## Impact

Reminder comments are remarks or reminders for yourself or your team members. Comments marked as **Is Reminder** may indicate important technical debt or unresolved issues.

## Why is this happening?

The comment has the **Is Reminder** property set to Yes. ODC Studio automatically sets the comments as reminders when you use the following keywords in upper case: TODO, TBD, REMINDER.

![A comment inlcuding the keyord TODO, with the Is Reminder property set to Yes.](images/reminder-comment-odcs.png "A comment set as Is Reminder")

## How to fix

Resolve the issue or finish the task related to the reminder comment. When completed, remove the comment or change **Is Reminder** to No. 

**Note:** Removing the keywords (TODO, TBD, REMINDER) from the comment doesn't automatically set the **Is Reminder** property to No.
