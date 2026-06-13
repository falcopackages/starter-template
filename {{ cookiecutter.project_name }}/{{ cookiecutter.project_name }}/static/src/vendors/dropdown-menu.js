(() => {
  const initDropdownMenu = (dropdownMenuComponent) => {
    const trigger = dropdownMenuComponent.querySelector(':scope > button');
    const popover = dropdownMenuComponent.querySelector(':scope > [data-popover]');
    const menu = popover.querySelector('[role="menu"]');

    if (!trigger || !menu || !popover) {
      const missing = [];
      if (!trigger) missing.push('trigger');
      if (!menu) missing.push('menu');
      if (!popover) missing.push('popover');
      console.error(`Dropdown menu initialisation failed. Missing element(s): ${missing.join(', ')}`, dropdownMenuComponent);
      return;
    }

    let menuItems = [];
    let activeIndex = -1;

    const closePopover = (focusOnTrigger = true) => {
      if (trigger.getAttribute('aria-expanded') === 'false') return;
      trigger.setAttribute('aria-expanded', 'false');
      trigger.removeAttribute('aria-activedescendant');
      popover.setAttribute('aria-hidden', 'true');

      if (focusOnTrigger) {
        trigger.focus();
      }

      setActiveItem(-1);
    };

    const openPopover = (initialSelection = false) => {
      document.dispatchEvent(new CustomEvent('basecoat:popover', {
        detail: { source: dropdownMenuComponent }
      }));

      // Position fixed popover when inside table-wrapper (for overflow-x: auto).
      if (dropdownMenuComponent.closest('.table-wrapper')) {
        const rect = trigger.getBoundingClientRect();
        const side = popover.dataset.side || 'bottom';
        const align = popover.dataset.align || 'start';

        popover.style.position = 'fixed';

        if (side === 'bottom') {
          popover.style.top = `${rect.bottom + 4}px`;
          popover.style.bottom = 'auto';
        } else if (side === 'top') {
          popover.style.bottom = `${window.innerHeight - rect.top + 4}px`;
          popover.style.top = 'auto';
        }

        if (align === 'end') {
          popover.style.right = `${window.innerWidth - rect.right}px`;
          popover.style.left = 'auto';
        } else {
          popover.style.left = `${rect.left}px`;
          popover.style.right = 'auto';
        }
      }

      trigger.setAttribute('aria-expanded', 'true');
      popover.setAttribute('aria-hidden', 'false');
      menuItems = Array.from(menu.querySelectorAll('[role^="menuitem"]')).filter(item =>
        !item.hasAttribute('disabled') &&
        item.getAttribute('aria-disabled') !== 'true'
      );

      if (menuItems.length > 0 && initialSelection) {
        if (initialSelection === 'first') {
          setActiveItem(0);
        } else if (initialSelection === 'last') {
          setActiveItem(menuItems.length - 1);
        }
      }
    };

    const setActiveItem = (index) => {
      if (activeIndex > -1 && menuItems[activeIndex]) {
        menuItems[activeIndex].classList.remove('active');
      }
      activeIndex = index;
      if (activeIndex > -1 && menuItems[activeIndex]) {
        const activeItem = menuItems[activeIndex];
        activeItem.classList.add('active');
        trigger.setAttribute('aria-activedescendant', activeItem.id);
      } else {
        trigger.removeAttribute('aria-activedescendant');
      }
    };

    trigger.addEventListener('click', () => {
      const isExpanded = trigger.getAttribute('aria-expanded') === 'true';
      if (isExpanded) {
        closePopover();
      } else {
        openPopover(false);
      }
    });

    dropdownMenuComponent.addEventListener('keydown', (event) => {
      const isExpanded = trigger.getAttribute('aria-expanded') === 'true';

      if (event.key === 'Escape') {
        if (isExpanded) closePopover();
        return;
      }

      if (!isExpanded) {
        if (['Enter', ' '].includes(event.key)) {
          event.preventDefault();
          openPopover(false);
        } else if (event.key === 'ArrowDown') {
          event.preventDefault();
          openPopover('first');
        } else if (event.key === 'ArrowUp') {
          event.preventDefault();
          openPopover('last');
        }
        return;
      }

      if (menuItems.length === 0) return;

      let nextIndex = activeIndex;

      switch (event.key) {
        case 'ArrowDown':
          event.preventDefault();
          nextIndex = activeIndex === -1 ? 0 : Math.min(activeIndex + 1, menuItems.length - 1);
          break;
        case 'ArrowUp':
          event.preventDefault();
          nextIndex = activeIndex === -1 ? menuItems.length - 1 : Math.max(activeIndex - 1, 0);
          break;
        case 'Home':
          event.preventDefault();
          nextIndex = 0;
          break;
        case 'End':
          event.preventDefault();
          nextIndex = menuItems.length - 1;
          break;
        case 'Enter':
        case ' ':
          event.preventDefault();
          menuItems[activeIndex]?.click();
          closePopover();
          return;
      }

      if (nextIndex !== activeIndex) {
        setActiveItem(nextIndex);
      }
    });

    menu.addEventListener('mousemove', (event) => {
      const menuItem = event.target.closest('[role^="menuitem"]');
      if (menuItem && menuItems.includes(menuItem)) {
        const index = menuItems.indexOf(menuItem);
        if (index !== activeIndex) {
          setActiveItem(index);
        }
      }
    });

    menu.addEventListener('mouseleave', () => {
      setActiveItem(-1);
    });

    menu.addEventListener('click', (event) => {
      if (event.target.closest('[role^="menuitem"]')) {
        closePopover();
      }
    });

    document.addEventListener('click', (event) => {
      if (!dropdownMenuComponent.contains(event.target)) {
        closePopover(false);
      }
    });

    document.addEventListener('basecoat:popover', (event) => {
      if (event.detail.source !== dropdownMenuComponent) {
        closePopover(false);
      }
    });

    dropdownMenuComponent.dataset.dropdownMenuInitialized = true;
    dropdownMenuComponent.dispatchEvent(new CustomEvent('basecoat:initialized'));
  };

  if (window.basecoat) {
    window.basecoat.register('dropdown-menu', '.dropdown-menu:not([data-dropdown-menu-initialized])', initDropdownMenu);
  }
})();
