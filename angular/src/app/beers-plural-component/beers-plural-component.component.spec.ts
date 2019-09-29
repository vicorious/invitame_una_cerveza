import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BeersPluralComponentComponent } from './beers-plural-component.component';

describe('BeersPluralComponentComponent', () => {
  let component: BeersPluralComponentComponent;
  let fixture: ComponentFixture<BeersPluralComponentComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BeersPluralComponentComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BeersPluralComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
