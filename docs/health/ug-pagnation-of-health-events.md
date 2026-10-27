> Source: https://docs.aws.amazon.com/health/latest/ug/pagnation-of-health-events.html
> Downloaded: 2026-10-27

# Viewing paginated lists of AWS Health events on EventBridge

AWS Health supports pagination of AWS Health events when the list of `resources` or `affectedEntities` causes the size of the message to exceed EventBridge’s 256KB message size limit. 

AWS Health includes all `resources` and `detail.affectedEntities` fields in the message. If this list of `resources` and `detail.affectedEntities` values exceeds 256KB, then AWS Health splits the health event into multiple pages and publish these pages as individual messages in EventBridge. Each page retains the same `eventARN` and `communicationId` values to help recombine the list of `resources` or `detail.affectedEntities` after all the pages are received.

These additional messages might cause unecessary messages, for example when the EventBridge rule is directed to a human readable interface such as email or chat. Customers with human readable notifications can add a filter for the `detail.page` field to process only the first page, which eliminates the unnecessary messages created from subsequent pages. 

In the schema, each communicationId includes the hyphenated page number after the communicationId, even when there is only 1 page. The fields `detail.page` and `detail.totalPages` describe the current page number and the total number of pages for the AWS Health event. The information contained in each paginated message is the same except for the list of `detail.affectedEntities` or `resources`. These lists can be reconstructed after all the pages are received. The pages of affected resources and entities are order-agnostic.
