app-ci YAML Pipeline Explanation
================================

This Azure pipeline is designed to trigger the documentation build process for the ``tudatpy`` project on ReadTheDocs upon completion of the ``tudatpy-feedstock`` pipeline. It selectively triggers based on updates to specific branches or tags.

**Pipeline Resources**
----------------------

The pipeline listens for completion events from the ``tudatpy-feedstock`` pipeline and triggers based on updates to the ``main`` and ``develop`` branches, or any tags.

.. list-table:: Trigger Conditions
   :widths: 20 30 50
   :header-rows: 1

   * - Resource Type
     - Condition
     - Description
   * - Branch
     - ``main``
     - Triggers a build with ``branches=stable`` to ensure documentation reflects the stable version.
   * - Branch
     - ``develop``
     - Triggers a build with ``branches=latest``, suitable for previewing upcoming changes.
   * - Tag
     - ``*``
     - Any tag triggers a build with ``branches=<tag name>``, allowing documentation to correspond directly to specific releases.

**Pipeline Steps**
------------------

The pipeline executes a shell script that dynamically sets the ``branches`` parameter for a POST request based on the source of the trigger:

1. Extract the reference type (branch or tag) and the specific name (branch name or tag name).
2. Set the default ``branchArg`` to "stable".
3. Adjust ``branchArg`` based on whether the source is a ``develop`` branch or a tag.
4. Send a POST request to the ReadTheDocs webhook with the appropriate token and branches parameter.

**Shell Script Logic Explained**

.. code-block:: bash

    refType=$(echo $(Build.SourceBranch) | cut -d'/' -f2)
    refName=$(echo $(Build.SourceBranch) | awk -F/ '{print $NF}')
    branchArg="stable"  # Default to stable for main branch
    if [ "$refType" = "heads" ]; then
        if [ "$refName" = "develop" ]; then
            branchArg="latest"
        fi
    elif [ "$refType" = "tags" ]; then
        branchArg="$refName"
    fi
    curl -X POST \
         -d "token=$(READTHEDOCS-TOKEN)" \
         -d "branches=$branchArg" \
         https://readthedocs.org/api/v2/webhook/tudatpy/200830/

This script ensures that documentation builds are correctly targeted, reflecting the latest developments from the ``develop`` branch, stable releases from the ``main`` branch, or specific tagged releases, enhancing the documentation's relevance and accuracy for different versions.
