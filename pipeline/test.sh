#!/usr/bin/env bash

- name: 'gcr.io/cloud-builders/gcloud'
  entrypoint: 'bash'
  args:
  - '-c'
  - |
    # File that contains failures.
    failure_file=failure.log
    touch ${failure_file}

    for d in ../component/*/; do

      config="${d}cloudbuild.yaml"

      if [[ ! -f "${config}" ]]; then
        echo "[X] - Component Build Warning: $d has no cloud build found"
      fi

      if [[ -f "${config}" ]]; then
        echo "[:] Component Build Status: ${config} found"
        echo "[:] Component Build Status: Building $d ... "
        (
          #logfile="${d::-1}.log" # Logfile for "foo/" builder is "foo.log".
          gcloud builds submit $d --config=${config} #> ${logfile} 2>&1
          exc="$?"
          echo $exc
          if [[ $exc -ne "0" ]]; then
            echo "[X] Component Build Status: ${config} Build Failed..."
            exit 1
          fi
        ) &

       fi
    done

    wait



    echo "[:] Component Build Status: All builds succeeded."