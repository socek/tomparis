# What is TomParis

TomParis it's a Python tool for generating and deploying kubernetes configs.

# Why not Helm ?

Helm is a project which aims to solve the same problem, but it has hard to use,
because it is using simple template system on top of the whitespace aware
language. This approach reading the Helm template files very hard to read. Also
it does not protect the developer against baddly formed YAML files.

# How the TomParis project is implemented

Every project is different and also the deployment is different. So this tool
should give possibility to decide on how to make the deploy.

We are trying to cut the Kubernetes YAML files into logical classes, so it
should be more simpler to make configuration using classes instead of YAML
files.

YAML is very suitable for settings. So we're using the YAML files only for the
settings/values, but the deploy script should decide in which order should the
settings files be read.

# Is it production ready?

Ufortunetly, no.

# What are disadvantages of TomParis tool ?

- If the TomParis has not implemented it yet, you will not be able to use the
feature. For example, we there will be no suitable class for ConfigMap, you
will not be able to use it using TomParis. `Helm` does not have such limitation.
- `Helm` is strong, becaus it have many Charts already implemented. We hope,
that in the future there will be some `Charts` for the TomParis to use.

# Who the hell is Tom Paris?

Tom Paris is a Helsmen on USS Voyager in Sci-Fi series "Star Trek: Voyager".
He is the first ever person in Star Trek who broke the "Warp 10 Barrier".
