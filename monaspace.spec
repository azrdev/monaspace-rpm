# Packaging template: packaging fonts, released as part of something else
#
# SPDX-License-Identifier: SIL
#
# This template documents spec declarations, used when packaging multiple font
# families, from a single dedicated source archive. The source rpm is named
# after the first (main) font family). Look up “fonts-3-sub” when the source
# rpm needs to be named some other way.
#
# It is part of the following set of packaging templates:
# “fonts-0-simple”: basic single-family fonts packaging
# “fonts-1-full”:   less common patterns for single-family fonts packaging
# “fonts-2-multi”:  multi-family fonts packaging
# “fonts-3-sub”:    packaging fonts, released as part of something else
#
BuildArch: noarch

# https://docs.fedoraproject.org/en-US/packaging-guidelines/SourceURL/#_release_example
%global forgeurl https://github.com/githubnext/monaspace/
%global tag      v%{version}
%forgemeta

Version: 1.000
Release: 1%{?dist}
License: OFL
URL:     %{forgeurl}

%global foundry           monaspace
%global fontlicenses      LICENSE

%global common_description %{expand:
The Monaspace type system is a monospaced type superfamily with some modern tricks up its sleeve. It consists of five variable axis typefaces. Each one has a distinct voice, but they are all metrics-compatible with one another, allowing you to mix and match them for a more expressive typographical palette.

✨ An exploration from GitHub Next. ✨ See the full story of Monaspace at monaspace.githubnext.com.
}



# do not use the zero/nosuffix declaration block, as this block
# will attempt to generate source rpm declarations by default.

# use variable/*.ttf variants from the source, since otf/*.otf seems to have many hard-parametrized files, instead of a single variable file
# and fedora refers to upstream: https://docs.fedoraproject.org/en-US/packaging-guidelines/FontsPolicy/#_tt_versus_cff

%global fontfamily1       Monaspace Neon
%global fontsummary1      GitHub Monaspace Neon: Neo-grotesque sans
%global fontpkgheader1    %{expand:
}
%global fonts1            fonts/variable/MonaspaceNeon*.ttf
#% global fontsex1          
%global fontconfs1        %{SOURCE11}
#% global fontconfsex1      
#% global fontappstreams1   
#% global fontappstreamsex1 
%global fontdescription1  %{expand:
%{common_description}
GitHub Monaspace Neon: Neo-grotesque sans
}

%global fontfamily2       Monaspace Argon
%global fontsummary2      GitHub Monaspace Argon: Humanist sans
%global fontpkgheader2    %{expand:
}
%global fonts2            fonts/variable/MonaspaceArgon*.ttf
%global fontconfs2        %{SOURCE12}
%global fontdescription2  %{expand:
%{common_description}
GitHub Monaspace Argon: Humanist sans
}

%global fontfamily3       Monaspace Xenon
%global fontsummary3      GitHub Monaspace Xenon: Slab serif
%global fontpkgheader3    %{expand:
}
%global fonts3            fonts/variable/MonaspaceXenon*.ttf
%global fontconfs3        %{SOURCE13}
%global fontdescription3  %{expand:
%{common_description}
GitHub Monaspace Xenon: Slab serif
}

%global fontfamily4       Monaspace Radon
%global fontsummary4      GitHub Monaspace Radon: Handwriting
%global fontpkgheader4    %{expand:
}
%global fonts4            fonts/variable/MonaspaceRadon*.ttf
%global fontconfs4        %{SOURCE14}
%global fontdescription4  %{expand:
%{common_description}
GitHub Monaspace Radon: Handwriting
}

%global fontfamily5       Monaspace Krypton
%global fontsummary5      GitHub Monaspace Krypton: Mechanical sans
%global fontpkgheader5    %{expand:
}
%global fonts5            fonts/variable/MonaspaceKrypton*.ttf
%global fontconfs5        %{SOURCE15}
%global fontdescription5  %{expand:
%{common_description}
GitHub Monaspace Krypton: Mechanical sans
}


Source0:  %{forgesource}
# fontconfig files, from /usr/share/fontconfig/templates/basic-font-template.conf
# TODO: parametrize from single template
Source11: 69-%{fontpkgname1}.conf
Source12: 69-%{fontpkgname2}.conf
Source13: 69-%{fontpkgname3}.conf
Source14: 69-%{fontpkgname4}.conf
Source15: 69-%{fontpkgname5}.conf

Name: monaspace
Summary:  Monaspace fonts by GitHub Next
%description
%wordwrap -v common_description

%fontpkg -a

%fontmetapkg

%prep
%setup
%linuxtext *.txt

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
%autochangelog
