#!/bin/bash

REPO="aupasana/vichara"
for ID in $(gh api --method GET "repos/$REPO/deployments?per_page=100" | jq -r ".[] | .id" | tr -d "\r")
do

    gh api -H "Accept: application/vnd.github+json" -H "X-GitHub-Api-Version: 2022-11-28" --method POST /repos/$REPO/deployments/$ID/statuses -f "state=inactive"
    gh api -H "Accept: application/vnd.github+json" -H "X-GitHub-Api-Version: 2022-11-28" --method DELETE /repos/$REPO/deployments/$ID
done

for ID in $(gh api --method GET "repos/$REPO/actions/runs?per_page=100" | jq -r ".workflow_runs[].id" | tr -d "\r")
do
    echo "Deleting workflow run ID: $ID"
    gh api -H "Accept: application/vnd.github+json" -H "X-GitHub-Api-Version: 2022-11-28" --method DELETE "/repos/$REPO/actions/runs/$ID"
done
