Name:           efivar
Version:        38
Release:        1
Summary:        Tools and libraries to work with EFI variables
License:        LGPL-2.1-only
URL:            https://github.com/rhboot/%{name}
Source0:        https://github.com/rhboot/%{name}/releases/download/%{version}/%{name}-%{version}.tar.bz2

Patch0001:      0001-Fix-the-march-issue-for-riscv64.patch
Patch0002:      0002-Fix-glibc-2.36-build-mount.h-conflicts.patch
%ifarch sw_64
Patch0003:      efivar-37-sw.patch
%endif

BuildRequires:  popt-devel glibc-static
BuildRequires:  gcc mandoc
Requires:       %{name}-libs = %{version}-%{release}

%description
Some command line interface of the UEFI variables tools are offered by %{name}.

%package        libs
Summary:        Libraries for %{name}

%description    libs
Libraries for %{name}.

%package        devel
Summary:        Development headers requred by libefivar
Requires:       %{name}-libs = %{version}-%{release}

%description    devel
Development titles to use libefivar must be included.

%package_help

%prep
%autosetup -n %{name}-%{version} -p1

%build
export LDFLAGS="-flto-partition=none"
%make_build

%install
%make_install
install -m 0644 src/abignore %{buildroot}%{_includedir}/efivar/.abignore

%ldconfig_scriptlets libs

%files
%defattr(-,root,root)
%license COPYING
%{_bindir}/*

%files libs
%defattr(-,root,root)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}/*.h
%{_includedir}/%{name}/.abignore
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libefiboot.so
%{_libdir}/libefivar.so
%{_libdir}/libefisec.so

%files help
%defattr(-,root,root)
%doc README.md
%{_mandir}/man1/*.1.gz
%{_mandir}/man3/*

%changelog
* Mon Nov 07 2022 zhouyihang <zhouyihang3@h-partners.com> - 38-1
- Type:requirements
- ID:NA
- SUG:NA
- DESC:update efivar to 38

* Wed Oct 19 2022 wuzx<wuzx1226@qq.com> - 37-9
- Type:feature
- CVE:NA
- SUG:NA
- DESC:Add sw64 architecture

* Mon May 16 2022 mylee <liweiganga@uniontech.com> - 37-8
- fix spec changelog date

* Thu Mar 24 2022 xinghe <xinghe2@h-partners.com> - 37-7
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix efibootmgr -v error

* Fri Jul 30 2021 gaihuiying <gaihuiying1@huawei.com> - 37-6
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix build error with gcc10

* Thu May 27 2021 lijingyuan <lijingyuan3@huawei.com> - 37-5
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:Add the compilation dependency of gcc.

* Tue Jun 9 2020 zhujunhao <zhujunhao8@huawei.com> - 37-4
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix gcc9 new warning -Werror=address-of-packed-member

* Mon Feb 17 2020 hexiujun <hexiujun1@huawei.com> - 37-3
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:unpack libs subpackage

* Thu Oct 17 2019 openEuler Buildteam <buildteam@openeuler.org> - 37-2
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:remove the libabigail in buildRequires.

* Mon Sep 2 2019 openEuler Buildteam <buildteam@openeuler.org> - 37-1
- Package init
