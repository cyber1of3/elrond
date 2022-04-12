#!/usr/bin/env python3 -tt
import os
from datetime import datetime

from rivendell.audit import print_done
from rivendell.audit import write_audit_log_entry


def ingest_splunk_data(
    verbosity,
    output_directory,
    case,
    stage,
    imgs,
    postpath,
    volatility,
    analysis,
    timeline,
):
    for img in imgs:
        if "vss" in img.split("::")[1]:
            vssimage = (
                "'"
                + img.split("::")[0]
                + "' ("
                + img.split("::")[1]
                .split("_")[1]
                .replace("vss", "volume shadow copy #")
                + ")"
            )
        else:
            vssimage = "'" + img.split("::")[0] + "'"
        print()
        print("     Indexing artefacts into Splunk for '{}'...".format(vssimage))
        entry, prnt = "{},{},{},indexing\n".format(
            datetime.now().isoformat(), vssimage, stage
        ), " -> {} -> indexing artfacts into {} for '{}'".format(
            datetime.now().isoformat().replace("T", " "),
            stage,
            vssimage,
        )
        write_audit_log_entry(verbosity, output_directory, entry, prnt)
        with open(
            "/" + postpath + "splunk/etc/apps/elrond/default/inputs.conf", "a"
        ) as inputsconf:
            if not os.path.exists(
                "/" + postpath + "splunk/etc/apps/elrond/default/inputs.conf"
            ):
                inputsconf.write("\n")
            else:
                pass
            if not img.split("::")[-1].endswith("memory"):
                for atftfile in os.listdir(
                    os.path.realpath(output_directory + img.split("::")[0])
                ):
                    if atftfile.endswith(".audit"):
                        inputsconf.write(
                            "[monitor://{}]\ndisabled = false\nhost = {}\nsourcetype = elrondCSV\nindex = {}\n\n".format(
                                os.path.realpath(output_directory + img.split("::")[0])
                                + "/"
                                + atftfile,
                                img.split("::")[0],
                                case,
                            )
                        )
                    else:
                        pass
                for atftroot, atftdirs, atftfiles in os.walk(
                    os.path.realpath(
                        output_directory + img.split("::")[0] + "/artefacts/cooked/"
                    )
                ):
                    for atftfile in atftfiles:
                        if os.path.isfile(os.path.join(atftroot, atftfile)):
                            if str(img.split("::")[-1])[1:].startswith("indows"):
                                if atftfile.endswith(
                                    "ShimCache.csv"
                                ) or atftfile.endswith("jumplists.csv"):
                                    sourcetype = "elrondCSV_noTime"
                                elif (
                                    atftfile.endswith("MFT.csv")
                                    or atftfile.endswith("History.csv")
                                    or atftfile.endswith("sqlite.csv")
                                ):
                                    sourcetype = "elrondCSV"
                                elif (
                                    (
                                        atftfile.endswith(".json")
                                        and "memory_" not in atftfile
                                    )
                                    and "registry" not in atftroot
                                    and "evt" not in atftroot
                                ):
                                    sourcetype = "elrondJSON"
                                else:
                                    sourcetype = ""
                            elif str(img.split("::")[-1])[1:].startswith("ac"):
                                if (
                                    (
                                        atftfile.endswith(".json")
                                        and "memory_" not in atftfile
                                    )
                                    and "logs" not in atftroot
                                    and "plists" not in atftroot
                                ):
                                    sourcetype = "elrondJSON"
                                elif atftfile.endswith("History.db.csv"):
                                    sourcetype = "elrondCSV"
                                else:
                                    sourcetype = ""
                            elif str(img.split("::")[-1])[1:].startswith("inux"):
                                if (
                                    (
                                        atftfile.endswith(".json")
                                        and "memory_" not in atftfile
                                    )
                                    and "logs" not in atftroot
                                    and "services" not in atftroot
                                ):
                                    sourcetype = "elrondJSON_noTime"
                                elif atftfile.endswith("sqlite.csv"):
                                    sourcetype = "elrondCSV"
                                else:
                                    sourcetype = ""
                            else:
                                sourcetype = ""
                            if sourcetype != "":
                                inputsconf.write(
                                    "[monitor://{}]\ndisabled = false\nhost = {}\nsourcetype = {}\nindex = {}\n\n".format(
                                        os.path.join(atftroot, atftfile),
                                        img.split("::")[0],
                                        sourcetype,
                                        case,
                                    )
                                )
                            else:
                                pass
                        else:
                            pass
                    for atftdir in atftdirs:
                        if os.path.isdir(os.path.join(atftroot, atftdir)):
                            if str(img.split("::")[-1])[1:].startswith("indows"):
                                if len(
                                    os.listdir(os.path.join(atftroot, atftdir))
                                ) > 0 and (atftdir == "registry" or atftdir == "evt"):
                                    inputsconf.write(
                                        "[monitor://{}/*]\ndisabled = false\nhost = {}\nsourcetype = elrondJSON\nindex = {}\n\n".format(
                                            os.path.join(atftroot, atftdir),
                                            str(img.split("::")[0]),
                                            case,
                                        )
                                    )
                                elif len(
                                    os.listdir(os.path.join(atftroot, atftdir))
                                ) > 0 and (atftdir == "IE"):
                                    inputsconf.write(
                                        "[monitor://{}/*]\ndisabled = false\nhost = {}\nsourcetype = elrondCSV_noTime\nindex = {}\n\n".format(
                                            os.path.join(atftroot, atftdir),
                                            str(img.split("::")[0]),
                                            case,
                                        )
                                    )
                                elif len(
                                    os.listdir(os.path.join(atftroot, atftdir))
                                ) > 0 and (
                                    atftdir == "edge"
                                    or atftdir == "chrome"
                                    or atftdir == "firefox"
                                ):
                                    inputsconf.write(
                                        "[monitor://{}/*]\ndisabled = false\nhost = {}\nsourcetype = elrondCSV_noTime\nindex = {}\n\n".format(
                                            os.path.join(atftroot, atftdir),
                                            str(img.split("::")[0]),
                                            case,
                                        )
                                    )
                                else:
                                    pass
                            else:
                                pass
                            if str(img.split("::")[-1])[1:].startswith("ac"):
                                if len(
                                    os.listdir(os.path.join(atftroot, atftdir))
                                ) > 0 and (atftdir == "logs" or atftdir == "plists"):
                                    inputsconf.write(
                                        "[monitor://{}/*]\ndisabled = false\nhost = {}\nsourcetype = elrondJSON\nindex = {}\n\n".format(
                                            os.path.join(atftroot, atftdir),
                                            str(img.split("::")[0]),
                                            case,
                                        )
                                    )
                                else:
                                    pass
                            else:
                                pass
                            if str(img.split("::")[-1])[1:].startswith("inux"):
                                if len(
                                    os.listdir(os.path.join(atftroot, atftdir))
                                ) > 0 and (atftdir == "logs" or atftdir == "services"):
                                    inputsconf.write(
                                        "[monitor://{}/*]\ndisabled = false\nhost = {}\nsourcetype = elrondJSON\nindex = {}\n\n".format(
                                            os.path.join(atftroot, atftdir),
                                            str(img.split("::")[0]),
                                            case,
                                        )
                                    )
                                else:
                                    pass
                            else:
                                pass
                        else:
                            pass
                if volatility and os.path.isdir(
                    os.path.realpath(output_directory + img.split("::")[0])
                    + "/artefacts/cooked/memory/"
                ):
                    inputsconf.write(
                        "[monitor://{}/artefacts/cooked/memory/*.json]\ndisabled = false\nhost = {}\nsourcetype = elrondJSON\nindex = {}\n\n".format(
                            os.path.realpath(output_directory + img.split("::")[0]),
                            img.split("::")[0],
                            case,
                        )
                    )
                    if os.path.exists(
                        str(os.path.realpath(output_directory + img.split("::")[0]))
                        + "/artefacts/cooked/memory/memory_timeliner.csv"
                    ):
                        inputsconf.write(
                            "[monitor://{}/artefacts/cooked/memory/memory_timeliner.csv]\ndisabled = false\nhost = {}\nsourcetype = elrondCSV\nindex = {}\n\n".format(
                                os.path.realpath(output_directory + img.split("::")[0]),
                                img.split("::")[0],
                                case,
                            )
                        )
                    else:
                        pass
                    if os.path.exists(
                        str(os.path.realpath(output_directory + img.split("::")[0]))
                        + "/artefacts/cooked/memory/iehistory"
                    ):
                        inputsconf.write(
                            "[monitor://{}/artefacts/cooked/memory/iehistory]\ndisabled = false\nhost = {}\nsourcetype = elrond_\nindex = {}\n\n".format(
                                os.path.realpath(output_directory + img.split("::")[0]),
                                img.split("::")[0],
                                case,
                            )
                        )
                    else:
                        pass
                else:
                    pass
                if analysis:
                    for atftroot, atftdirs, atftfiles in os.walk(
                        os.path.realpath(
                            output_directory + img.split("::")[0] + "/analysis/"
                        )
                    ):
                        for atftfile in atftfiles:
                            if img.split("::")[0] in atftroot and os.path.isfile(
                                os.path.join(atftroot, atftfile)
                            ):
                                if atftfile.endswith(
                                    "analysis.csv"
                                ) or atftfile.endswith("IOCs.csv"):
                                    inputsconf.write(
                                        "[monitor://{}]\ndisabled = false\nhost = {}\nsourcetype = elrondCSV\nindex = {}\n\n".format(
                                            os.path.join(atftroot, atftfile),
                                            str(img.split("::")[0]),
                                            case,
                                        )
                                    )
                                else:
                                    pass
                            else:
                                pass
                else:
                    pass
                if timeline:
                    for timeroot, _, timefiles in os.walk(
                        os.path.realpath(
                            output_directory + img.split("::")[0] + "/artefacts/"
                        )
                    ):
                        for timefile in timefiles:
                            if img.split("::")[0] in timeroot and os.path.isfile(
                                os.path.join(timeroot, timefile)
                            ):
                                if timefile.endswith("plaso_timeline.csv"):
                                    inputsconf.write(
                                        "[monitor://{}]\ndisabled = false\nhost = {}\nsourcetype = elrondCSV\nindex = {}\n\n".format(
                                            os.path.join(timeroot, timefile),
                                            str(img.split("::")[0]),
                                            case,
                                        )
                                    )
                                else:
                                    pass
                            else:
                                pass
                else:
                    pass
            elif img.split("::")[-1].endswith("memory") and "memory_" in str(
                os.listdir(os.path.realpath(output_directory + img.split("::")[0]))
            ):
                inputsconf.write(
                    "[monitor://{}/*.json]\ndisabled = false\nhost = {}\nsourcetype = elrondJSON\nindex = {}\n\n".format(
                        os.path.realpath(output_directory + img.split("::")[0]),
                        img.split("::")[0],
                        case,
                    )
                )
                if os.path.exists(
                    str(os.path.realpath(output_directory + img.split("::")[0]))
                    + "/memory_timeliner.csv"
                ):
                    inputsconf.write(
                        "[monitor://{}/memory_timeliner.csv]\ndisabled = false\nhost = {}\nsourcetype = elrondCSV\nindex = {}\n\n".format(
                            os.path.realpath(output_directory + img.split("::")[0]),
                            img.split("::")[0],
                            case,
                        )
                    )
                else:
                    pass
                if os.path.exists(
                    str(os.path.realpath(output_directory + img.split("::")[0]))
                    + "/iehistory"
                ):
                    inputsconf.write(
                        "[monitor://{}/iehistory]\ndisabled = false\nhost = {}\nsourcetype = elrond_\nindex = {}\n\n".format(
                            os.path.realpath(output_directory + img.split("::")[0]),
                            img.split("::")[0],
                            case,
                        )
                    )
                else:
                    pass
            else:
                pass
        with open(
            "/" + postpath + "splunk/etc/apps/elrond/default/tags.conf", "a"
        ) as tagsconf:
            if (
                img.split("::")[0].endswith(".E01")
                or img.split("::")[0].endswith(".e01")
                or img.split("::")[0].endswith(".VMDK.raw")
                or img.split("::")[0].endswith(".vmdk.raw")
            ):
                imgtype = "\ndisk = enabled"
            else:
                imgtype = "\nmemory = enabled"
            if img.split("::")[1].startswith("Windows") or img.split("::")[
                1
            ].startswith("windows"):
                imgtype = imgtype + "\nWindows = enabled\n\n"
            elif img.split("::")[1].startswith("Mac") or img.split("::")[1].startswith(
                "mac"
            ):
                imgtype = imgtype + "\nmacOS = enabled\n\n"
            elif img.split("::")[1].startswith("Linux") or img.split("::")[
                1
            ].startswith("linux"):
                imgtype = imgtype + "\nLinux = enabled\n\n"
            else:
                pass
            tagsconf.write("[host={}]{}".format(img.split("::")[0], imgtype))
        output_directory = os.path.dirname(output_directory) + "/"
        if os.path.exists(
            "/" + postpath + "splunk/etc/apps/elrond/default/tags.conf.orig.pre41"
        ):
            os.remove("/" + postpath + "splunk/etc/apps/elrond/default/tags.conf")
            os.rename(
                r"/" + postpath + "splunk/etc/apps/elrond/default/tags.conf.orig.pre41",
                r"/" + postpath + "splunk/etc/apps/elrond/default/tags.conf",
            )
        else:
            pass
        print_done(verbosity)
        print("     Splunk indexing completed for '{}'".format(vssimage))
        entry, prnt = "{},{},{},completed\n".format(
            datetime.now().isoformat(), vssimage, stage
        ), " -> {} -> indexed artfacts into {} for '{}'".format(
            datetime.now().isoformat().replace("T", " "),
            stage,
            vssimage,
        )
        write_audit_log_entry(verbosity, output_directory, entry, prnt)
