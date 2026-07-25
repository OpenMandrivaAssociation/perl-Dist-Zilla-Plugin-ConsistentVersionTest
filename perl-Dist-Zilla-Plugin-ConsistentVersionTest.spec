%define upstream_name    Dist-Zilla-Plugin-ConsistentVersionTest
%define upstream_version 0.03

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	Adds a release test to ensure that all modules have the same $VERSION
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/RsrchBoy/Dist-Zilla-Plugin-ConsistentVersionTest
Source0:	https://cpan.metacpan.org/authors/id/R/RS/RSRCHBOY/Dist-Zilla-Plugin-ConsistentVersionTest-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla)
BuildRequires:	perl(Test::ConsistentVersion)
BuildArch:	noarch

%description
This is an extension of the Dist::Zilla::Plugin::InlineFiles manpage,
providing the following files

  xt/release/consistent-version.t

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*


